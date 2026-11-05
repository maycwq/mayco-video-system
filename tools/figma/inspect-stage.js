// leitura de stage temporal no Figma (somente leitura).
//
// foi assim que as evidências EV-R0x-xx desta base foram coletadas. cola no use_figma do Figma MCP
// (ou num plugin de desenvolvimento), troca PAGE_ID, ROOT_ID, PROFUNDIDADE e PULAR, e lê o retorno.
// o script não cria, não move e não apaga nada. não chama setPluginData nem altera propriedades.
//
// saída: uma linha por nó
//   <id> <tipo> "<nome>" @x,y LxA [HID] [op] [rot] [fill de vídeo/imagem] T"texto" <fonte/estilo/tamanho> {keyframes}
// keyframes compactos por propriedade: OP (opacidade), TXY (translação), SXY (escala), ROT, W, H
//   cada keyframe vira <tempo><easing>=<valor>; easing: h (HOLD, corte), l, eo (ease out), ei, eio, cb(x1,y1,x2,y2), sp (spring)
//
// limites conhecidos:
//   - o retorno do use_figma tem teto de ~48 KB; use PROFUNDIDADE baixa e PULAR para subárvores grandes (legendas)
//   - alguns tipos de keyframe podem falhar ao serializar; o script ignora a propriedade e segue
//   - get_motion_context no frame raiz pode devolver timelineDurationMs nulo; a duração real está em node.animations[*].timelineDuration

const PAGE_ID = '182:2964';
const ROOT_ID = '188:2964';
const PROFUNDIDADE = 2;
const PULAR = [];          // ids cujos filhos não devem ser listados
const LIMITE = 44000;      // caracteres

const E = {HOLD:'h', LINEAR:'l', EASE_OUT:'eo', EASE_IN:'ei', EASE_IN_AND_OUT:'eio', CUSTOM_CUBIC_BEZIER:'cb', SPRING:'sp'};
const P = {OPACITY:'OP', ROTATION:'ROT', TRANSLATION_XY:'TXY', SCALE_XY:'SXY', WIDTH:'W', HEIGHT:'H'};
const r = v => Math.round(v * 100) / 100;
function val(v) { try { const x = v.value; if (typeof x === 'number') return r(x); if (x && 'x' in x) return r(x.x) + ',' + r(x.y); return '?'; } catch (e) { return '?'; } }
function ease(e) {
  if (!e) return '';
  let s = E[e.type] || e.type;
  if (e.type === 'CUSTOM_CUBIC_BEZIER' && e.easingFunctionCubicBezier) { const b = e.easingFunctionCubicBezier; s += '(' + [b.x1, b.y1, b.x2, b.y2].map(r).join(',') + ')'; }
  return s;
}
function kf(n) {
  let k; try { k = n.manualKeyframeTracks; } catch (e) { return ''; }
  if (!k) return '';
  const partes = [];
  for (const p of Object.keys(k)) {
    try { partes.push((P[p] || p) + ':' + k[p].keyframes.map(f => r(f.timelinePosition) + ease(f.easing) + '=' + val(f.value)).join(' ')); } catch (e) { partes.push(p + ':?'); }
  }
  return partes.length ? ' {' + partes.join(' | ') + '}' : '';
}
function fill(n) {
  try {
    if (!('fills' in n) || !Array.isArray(n.fills)) return '';
    const a = n.fills.filter(f => f.type === 'VIDEO' || f.type === 'IMAGE').map(f => f.type[0] + '#' + (f.videoHash || f.imageHash || '').slice(0, 6) + (f.visible === false ? '(off)' : '') + (f.scaleMode ? '/' + f.scaleMode : ''));
    return a.length ? ' [' + a.join(',') + ']' : '';
  } catch (e) { return ''; }
}
function txt(n) {
  if (n.type !== 'TEXT') return '';
  let f = '';
  try { const s = new Set(n.getStyledTextSegments(['fontName', 'fontSize']).map(g => g.fontName.family + '/' + g.fontName.style + '/' + r(g.fontSize))); f = [...s].slice(0, 3).join(';'); } catch (e) {}
  return ' T"' + n.characters.replace(/\n/g, '⏎').slice(0, 70) + '" <' + f + '>';
}
function linha(n, d) {
  return '  '.repeat(d) + n.id + ' ' + n.type.slice(0, 4) + ' "' + n.name.slice(0, 110) + '" @' + Math.round(n.x) + ',' + Math.round(n.y) + ' ' + Math.round(n.width) + 'x' + Math.round(n.height)
    + (n.visible === false ? ' HID' : '') + (('opacity' in n && n.opacity !== 1) ? ' op' + r(n.opacity) : '') + (n.rotation ? ' rot' + r(n.rotation) : '') + (n.isMask ? ' MASK' : '')
    + fill(n) + txt(n) + kf(n);
}
function dump(root) {
  const L = []; let tamanho = 0, cortado = null;
  (function w(n, d) {
    if (cortado) return;
    const s = linha(n, d); tamanho += s.length;
    if (tamanho > LIMITE) { cortado = n.id; return; }
    L.push(s);
    if (d < PROFUNDIDADE && 'children' in n && !PULAR.includes(n.id)) { for (const c of n.children) w(c, d + 1); }
    else if ('children' in n && n.children.length) { L.push('  '.repeat(d + 1) + '… ' + n.children.length + ' filhos / ' + n.findAll(() => true).length + ' descendentes'); }
  })(root, 0);
  return L.join('\n') + (cortado ? '\nCORTADO EM ' + cortado : '');
}

const page = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(page);
const raiz = await figma.getNodeByIdAsync(ROOT_ID);
let duracoes = new Set();
for (const n of [raiz, ...raiz.findAll(() => true)]) {
  try { const a = n.animations; if (a) for (const v of Object.values(a)) if (v.timelineDuration) duracoes.add(r(v.timelineDuration)); } catch (e) {}
}
return 'timelineDuration: ' + [...duracoes].join(', ') + '\n' + dump(raiz);

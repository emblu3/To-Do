/*
 * Created by ? (DreamTek) on (9/2/2014).
 * Source: https://stackoverflow.com/questions/454202/creating-a-textarea-with-auto-resize
 */

var tx = document.getElementsByTagName('textarea');
for (var i = 0; i < tx.length; i++) {
  tx[i].setAttribute('style', 'height:' + (tx[i].scrollHeight) + 'px;overflow-y:hidden;');
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput(e) {
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';
}



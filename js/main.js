import * as bootstrap from "bootstrap";
import emphasizeLines from "./emphasize-lines.js";

document.querySelectorAll('[data-bs-toggle="popover"]').forEach((popover) => {
  new bootstrap.Popover(popover);
});

(() => {
  emphasizeLines();
})();

// Help make styling emphasized lines easier. Find all span.hll elements and
// set their parent's class to `emphasized`.
export default function emphasizeLines() {
  document.querySelectorAll("span.hll").forEach((element) => {
    const parent = element.parentElement;
    !parent.classList.contains("emphasized") &&
      parent.classList.add("emphasized");
  });
}

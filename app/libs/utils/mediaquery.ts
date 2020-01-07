
let mql: MediaQueryList | null = null;

export default function getMQL(): MediaQueryList {
  if (mql === null) {
    mql = window.matchMedia(`(min-width: 800px)`);
  }
  return mql;
}

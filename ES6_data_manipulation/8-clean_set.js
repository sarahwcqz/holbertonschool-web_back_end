export default function cleanSet(mySet, startString) {
  if (!(mySet instanceof Set) || typeof startString !== 'string' || startString === '') {
    return '';
  }

  const result = [];

  for (const value of mySet) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      result.push(value.slice(startString.length));
    }
  }

  return result.join('-');
}

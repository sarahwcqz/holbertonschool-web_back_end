export default function updateUniqueItems(myMap) {
  if (!(myMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of myMap) {
    if (value === 1) {
      myMap.set(key, 100);
    }
  }

  return myMap;
}

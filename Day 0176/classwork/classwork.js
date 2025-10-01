function getMostFrequent(json) {
    return json.temperature.map(day => {
    const freq = {};
    let max = 0;

    day.forEach(temp => {
      freq[temp] = (freq[temp] || 0) + 1;
      if (freq[temp] > max) max = freq[temp];
    });

    for (let i = day.length - 1; i >= 0; i--) {
      if (freq[day[i]] === max) return day[i];
    }
  });
}
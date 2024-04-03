import numpy as np

arr = np.array([
3.6, 5.1, 6.7, 7.3, 7.6,
9.9, 10.0, 10.1, 12.3, 12.6,
15.0, 15.7, 23.7, 24.2, 24.6,
31.8, 32.2, 33.7, 35.0, 36.8
])

# Calculate required parameters
max_val = np.max(arr)
min_val = np.min(arr)
data_range = max_val - min_val
count_data = arr.size
k = 1 + 3.322 * np.log10(count_data)
k_int = int(k)
w = data_range / k_int
rounded_w = round(w, 2)

print("Min: ", min_val)
print("Max: ", max_val)
print("Range: ", data_range)
print("Count: ", count_data)
print("Intervalos (k): ", k)
print("Intervalos (k): ", k_int)
print("Amplitud (w): ", w)
print("Amplitud (w): ", rounded_w)


# Calculate class intervals
intervals = [(min_val + i * w, min_val + (i + 1) * w) for i in range(k_int)]
intervals = [(round(start, 2), round(end, 2)) for start, end in intervals]

# Calculate class marks
class_marks = [round((start + end) / 2, 2) for start, end in intervals]

# Calculate frequency (fi)
freq = [np.sum((arr >= start) & (arr < end)) for start, end in intervals]

# Calculate relative frequency (hi)
rel_freq = [f / count_data for f in freq]

# Calculate cumulative frequency (Fi)
cum_freq = np.cumsum(freq)

# Calculate cumulative relative frequency (Hi)
cum_rel_freq = np.cumsum(rel_freq)

# Print the table
print("Tiempo de atención (min)\tMarca de clase\tfi\t\thi\t\tFi\tHi")
for i in range(k_int):
    print(f"{intervals[i][0]} - {intervals[i][1]}\t\t\t{class_marks[i]}\t\t{freq[i]}\t\t{rel_freq[i]:.2f}\t\t{cum_freq[i]}\t{cum_rel_freq[i]:.2f}")
# https://www.educative.io/collection/page/5668639101419520/5671464854355968/6658855733821440

def find_averages_of_subarrays(K, arr):
  result = []
  for i in range(len(arr)-K+1):
    # find sum of next 'K' elements
    _sum = 0.0
    for j in range(i, i+K):
      _sum += arr[j]
    result.append(_sum/K)  # calculate average

  return result


def find_averages_of_subarrays_2(K, arr):
  result = []

  _sum = 0
  for i in range(K):
      _sum += arr[i]

  result.append(_sum/K)

  for i in range(1, len(arr)-K+1):
    _sum = _sum - arr[i-1] + arr[i+K-1]
    result.append(_sum / K)

  return result


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

  result = find_averages_of_subarrays_2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))

main()
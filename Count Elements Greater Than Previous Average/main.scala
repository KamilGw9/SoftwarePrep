def countResponseTimeRegressions(responseTimes: Seq[Int]): Int = {
  var count = 0
  var prefixSum = 0

  for (i <- responseTimes.indices) {
    if (i > 0) {
      val average = prefixSum.toDouble / i
      if (responseTimes(i) > average) {
        count += 1
      }
    }
    prefixSum += responseTimes(i)
  }

  count
}
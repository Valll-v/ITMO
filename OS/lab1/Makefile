TIMEOUT_FLAG = --timeout 60s
COUNT = 1
CPU_PARAM = callfunc
CACHE_PARAM = l1cache-line-size


cpu:
	stress-ng --cpu $(COUNT) --cpu-method $(CPU_PARAM) $(TIMEOUT_FLAG) &
	pidstat 3 --human | grep -e "%CPU" -e stress-ng

cache:
	free -m
	stress-ng $(CACHE_PARAM) $(COUNT) $(TIMEOUT_FLAG) &
	free -s 2 -m

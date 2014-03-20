# By default haddop sorts keys lexicographically before sending the output of the map phase as input to the reduce phase.
# We have to specify the comparator and the option for numeric sort in this example.

hadoop dfs -rmr /user/sadhikar/weblog/histogram_links
hadoop jar /usr/lib/hadoop/contrib/streaming/hadoop-streaming-1.0.3-Intel.jar \
	-D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator \
	-D  mapred.text.key.comparator.options=-n \
	-file ./histogram_links_mapper.py \
	-file ./histogram_links_reducer.py \
	-mapper ./histogram_links_mapper.py \
	-reducer ./histogram_links_reducer.py \
	-input /user/sadhikar/weblog/input \
	-output /user/sadhikar/weblog/histogram_links


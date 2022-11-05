# pavements
A configuration tool for paragraph

Paragraph relies on a single graph representing software/system configuration parameters and their "containers".
https://github.com/incodame/paragraph/blob/master/paragraph.yml

However this data structure can become overly complex when trying to analyze dependencies across several contexts
- size is not any more manageable
- parts of the graph ("fragments", "tiles" or "views") are dependent on the versions of described software/systems
- combining fragments of this graph to create a correct representation is subject to some contraints

The goal of this foundation tool is to allow the creation of such a combined graph representation using a 
user friendly set of incremental commands.


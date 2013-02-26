#WhoSampledWho?
- - -

## What?

This projects visualizes how (musical) artists sample and cover other artists. The data is 
drawn from the great website [SecondHandSongs](http:www.secondhandsongs.com)! In total, there 
are about 250k performances on the website, but because of API restrictions the visualization 
only covers about 10k performances (so far). 

A good way to think of this is as a graph structure where artists are nodes and edges are 
directed. As weights, I use the amount of times a certain artist covers/samples another artist. 
The data are collected in python dictionaries and then written to csv-files that serve as input 
for the gephi software. 

## Results?

There are four main visualizations:
* Artists that cover other artists. 
* Artists that are being covered by other artists.
* Artists that sample other artists.
* Artists that are being sampled by other artists. 



![Artists that cover](https://raw.github.com/pdevlieger/WhoSampledWho/master/covers_10000.png)

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/covered_10000.png)

![Artists that sample](https://raw.github.com/pdevlieger/WhoSampledWho/master/samples_10000.png)

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/sampled_10000.png)


## Final thoughts?

First of all, many thanks to the people at [SecondHandSongs](http:www.secondhandsongs.com)! The 
website is really fun to browse through and much of the information online is incredibly accurate. 

Second, there are some issues to keep in mind when looking at these graphics. 
* The data is not necessarily completely accurate. As with any top down project, it is possible 
that there are some duplicates, missing _covered_ or _sampled_ flags in the dataset.
* The website has more information about covers than about samples that are being used. Therefore, 
it is likely that most of these issues are present in the datasets I collected for sampled music.
* The graphs only cover information of about 10k performances, even though there are about 250k 
data points to collect. This is only about 4% of the dataset, but results will be updated in the 
future!

Third, there are a couple of projects that I could be working on in the future.
* I would like to see if it is possible to store everything in a database and find the shortest 
path between two artists.
* Write a program that suggests samples the way facebook or linkedin looks at closing triangles?
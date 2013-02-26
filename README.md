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

This graph present nodes proportionally to the amount of covers the artists has performed. This means 
that artists with larger nodes have covered many songs from other artists. The most avid cover artists 
(e.g. Frank Sinatra or Ella Fitzgerald) seem to be 'from back in the days', but overall quite many artists 
seem to resort to covers.

![Artists that cover](https://raw.github.com/pdevlieger/WhoSampledWho/master/covers_10000.png)

When looking at the artists that are _being_ covered, it is clear that most of the covers come from some 
key artists. The frontrunners are the Beatles with 12 songs that have been covered. Hiram Sherman, 
Frances Mercer, Hollis Shaw and Ralph Stuart only have one song that was covered; All the Things You Are, 
performed in the 1939 musical Very Warm for May, that later became a very popular jazz song. Overall, there 
are much less artists that are being covered than artists that cover.

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/covered_10000.png)

What about samples? Overall, there are not that many artists that sample. De La Soul, Public Enemy and 
A Tribe Called Quest are definitely very avid sampling artists. But who do they sample?

![Artists that sample](https://raw.github.com/pdevlieger/WhoSampledWho/master/samples_10000.png)

There are quite many artists that are being sampled! Not surprisingly, much of these artists are funk and soul 
artists from the seventies. Especially when we take away artists that have at least 2 edges (where an edge is 
defined as a sample), the field becomes a bit more sparse. The biggest surprise for me here were Pink Floyd and 
the Steve Miller Band. 

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/sampled_10000.png)

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/sampled_10000_2edges.png)

There are also some artists that really like each other. 

![Artists that are covered](https://raw.github.com/pdevlieger/WhoSampledWho/master/turbonegro.png)
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
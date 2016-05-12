# VISA-Free

Leaping off from the point of "visualizing the networks between countries and continents imposed by visa status", one can imagine multitudes of visualizations: force-layout, Sankey-diagram, sunburst, etc. One that jumped out as a possibly interesting approach was a hive-plot.

One immediate advantage to the hive plot, is the way it both naturally handles grouping, but shows all of the edges and spreads them out. In our case, we do have a natural clustering on nodes(the countries) given by continents. Next, one observes that there are four statuses that a visa between two countries can take: `free, on-arrival, required, refused`. One can imagine that `free` means that no visa is required, `on-arrival` means that no prior arrangements are needed, `required` means that one must arrange ahead of time, and `refused` is, well, a special designation when a passport is not permitted entry to a country or territory. One might immediately guess that a hive plot with seven "arms" corresponding to seven continents(we seprate Central America into its own, but exclude Antarctica), and colored edges to represent the four statuses. However, let's take a minute to compute:

```
222^2=49284
``` 

that's a LOT of edges. Additionally, because countries share continents, there are edges between nodes on a single axis as well(this would take the form of another visualization called a Chord Diagram). For the purpose of producing a beautiful picture, this might be appropriate, for the purpose of a meaningful data visualization, this falls seriously short. So next one might attempt to reduce the dataset to something more manageable, and this is where the hard work comes in. 

## Reducing the data set

A first attempt at reducing the data set would be a similar visualization to before, but only showing one status at a time. Given that `refused` status is rare for most countries, one could think of this producing four visualizations, three of which are rougly `50k/3~16k` and one of considerably smaller size. Unfortunately, `16k` is still quite too large, and in fact the `free` and `on-arrival` graphs actually take the lion's share. Additionally, we still have the issue of edges between countries on the same continent. 

Reducing the dataset to something managable requires us to change the structure of our visualization a bit. Stepping away from the assumption that "arms" should correspond to individual continents, we can actually find a better way: by considering arms for each status, and only considering two continents at a time. 

This means that there will be `7^2=49` visualizations(one for each pair, allowing for a pair of the same continent). We designate one of the pair's elements to be the source continent, and the other to be the destination. Now we fan the destination continent's countries over the four axes based on the status of the visa to that country. The primary axis at zero degrees represents the source or "origin". We still color based on status for readability, and to create a clear correlation between amount of a color on the graph, and the frequency of that status in the continent pair. Note that we only draw nodes that have at least one edge incedent on them. In the case where a country has no relationships(edges) of a particular visa-status, that country will not appear as a node on that axis of the visualization.

## Style Choices

We chose primary colors because the number of necessary colors was small. We expanded the `origin` axis and scaled other axes to reasonably provide room for the corresponding numbers of nodes.

## Interactions for more information

First, the user needs to be able to select the continent pair, so two drop downs select source and target continents. Additionally, there is actually more information than the four options of visa status. In reality, the visa status also has information about `term` and additional `notes`. The `term` field is how long the visa actually lasts for. The `notes` information is additional requirements, cautions, and useful reminders that might be less common, and are important for any travelers to that country. These appear on mouseover, as to allow the graph to remain approachable, but reveal the full richness of the data. Also on mouseover, a stroke is applied to the node an all incident edges. This is to allow for a summary of the `local network` of that node given by visas. 

An additional feature would be to add an accompanying pie chart along side the hive plot so that one could see the shares of the world population "open" to a traveler starting from one country, with the various statuses.
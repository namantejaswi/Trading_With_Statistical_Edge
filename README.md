# Trading_With_Statistical_Edge 💸 🤑
We explore how certain statistical concepts can help us become a better trader

Refer this article written to explain the workings

https://medium.com/coinmonks/trading-with-a-statistical-edge-2afea137b261


## Monte Carlo Simulation 🎲
This project aims to uderstand the mathematics/statistics behind gambling and apply the learnings to a favourable betting enviroment with an edge like trading

First and foremost we need to understand the Law of Large Numbers and Expected Value

Expected value is the probablistic mathematical outcome of a event for a single instance

say we have an event X with discrete outcomes O1 and O2, having probabilities p1 and p2 then the expected value of event E will be

E(x)=P1O1+P2O2

For instance consider a fair dice with numbers 1 to 6, what is the expected value?

Given our premise that we have a fair dice at hand each nmber is equally likelly to turn up, so

E(x)=1/6[1+2+3+4+5+6] E(x)=3.5

Now on roll of the dice it is impossible to get 3.5, this where the law of large number plays its it part it states that,

The outcome of the event will converge to its expected value as we repeat the event/experiment.

This means that as we continue rolling the dice many times the mean of our outcomes will approach 3.5.

NOTE- In a linearlly equidistant outcome such as this the expected value will be the same as median. Further this stochastic process can be modelled as a normal distribution

The crux is, one may flip a coin 10 times and get 8 heads, but if one continues to flip the coin 1000 times it is unlikelly he will get 800 heads and the outcomes is more likely to be 50:50 and as we repeat our experiment the observed value will converge to the expected value.

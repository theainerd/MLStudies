# An overview of gradient descent optimization algorithms

Gradient descent is one of the most popular algorithms to perform optimization and by far the most common way to optimize neural networks.

## Gradient descent variants
There are three variants of gradient descent, which differ in how much data we use to compute the gradient of the objective function

* **Batch gradient descent** : Vanilla gradient descent, aka batch gradient descent, computes the gradient of the cost function w.r.t.
to the parameters θ for the entire training datase. As we need to calculate the gradients for the whole dataset to perform just one update, batch gradient
descent can be very slow and is intractable for datasets that do not fit in memory.</br>
**Note** : Batch gradient descent is guaranteed to converge to the global minimum for convex error surfaces and to a local minimum for non-convex surfaces.

* **Stochastic gradient descent** : Stochastic gradient descent (SGD) in contrast performs a parameter update for each training example.

* **Mini-batch gradient descent** : Mini-batch gradient descent finally takes the best of both worlds and performs an update for every
mini-batch of n training examples.

## Gradient descent optimization algorithms

In the following, we will outline some algorithms that are widely used by the Deep Learning
community to deal with the aforementioned challenges.
### Momentum

Momentum is a method that helps accelerate SGD in the relevant direction and dampens oscillations. It does this by adding a fraction γ of the update vector of the
past time step to the current update vector.

### Adagrad

Adagrad is an algorithm for gradient-based optimization that does just this: It adapts the learning
rate to the parameters, performing larger updates for infrequent and smaller updates for frequent
parameters. For this reason, it is well-suited for dealing with sparse data.

One of Adagrad’s main benefits is that it eliminates the need to manually tune the learning rate. Most
implementations use a default value of 0.01 and leave it at that.

Adagrad’s main weakness is its accumulation of the squared gradients in the denominator: Since
every added term is positive, the accumulated sum keeps growing during training. This in turn causes
the learning rate to shrink and eventually become infinitesimally small, at which point the algorithm
is no longer able to acquire additional knowledge. The following algorithms aim to resolve this flaw.

### Adadelta

Adadelta is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing
learning rate. Instead of accumulating all past squared gradients, Adadelta restricts the window of
accumulated past gradients to some fixed size w.

With Adadelta, we do not even need to set a default learning rate, as it has been eliminated from the
update rule.

### RMSProp

RMSprop is an unpublished, adaptive learning rate method proposed by Geoff Hinton. RMSprop and Adadelta have both been developed independently around the same time stemming
from the need to resolve Adagrad’s radically diminishing learning rates. RMSprop in fact is identical
to the first update vector of Adadelta.

### Adam (RMSProp + Momentum)

Adam can be viewed as a combination of RMSprop and momentum: RMSprop contributes the exponentially decaying average of past squared gradients, while momentum
accounts for the exponentially decaying average of past gradients.

In summary, **RMSprop** is an **extension of Adagrad** that deals with its radically diminishing learning
rates. It is **identical to Adadelta**, except that Adadelta uses the RMS of parameter updates in the
numerator update rule. Adam, finally, **adds bias-correction and momentum to RMSprop**. Insofar,
RMSprop, Adadelta, and Adam are very similar algorithms that do well in similar circumstances.show that its bias-correction helps Adam slightly outperform RMSprop towards
the end of optimization as gradients become sparser. Insofar, **Adam** might be the best overall choice.

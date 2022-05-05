#!/usr/bin/env python
# coding: utf-8

#  ## we will use 'pykeen' library to train our TransE model.
#  Pykeen stands for 'Python KnowlEdge EmbeddiNgs'.
#  Pykeen is a python package that generates knowledge graph embeddings while abstracting away the training loop 
#  and evaluation. It is stable, easy to work with and well documented.
#  https://pykeen.readthedocs.io/en/stable/installation.html



import matplotlib # For graph plotting
from pykeen.pipeline import pipeline

# Import pykeen library
import pykeen
from pykeen.models.predict import get_head_prediction_df
from pykeen.models.predict import get_all_prediction_df
from pykeen.models.predict import get_tail_prediction_df
from pykeen.models.predict import get_relation_prediction_df
# 'Nations' dataset ships & installs with pykeen
# In Windows, it is found under the python directory, for example:
# C:\Users\USER\AppData\Roaming\Python\Python38\site-packages\pykeen\datasets\nations
from pykeen.datasets import Nations


#from pykeen.pipeline import pipeline
dataset = Nations()
training_triples_factory = dataset.training

# Pick a model, TransE in our case
from pykeen.models import TransE
model = TransE(triples_factory=training_triples_factory)


# Pick an optimizer from Torch
# Adam: Adaptive Moment Estimation is an algorithm for optimization technique for gradient descent
from torch.optim import Adam
optimizer = Adam(params=model.get_grad_params())


# ## Pick a training approach (sLCWA or LCWA)
# Whenever we have a knowledge graph we need to make certain assumptions to draw inferences from it. 
# Closed World Assumption is one such assumption. It assumes that if a link is not present between two entities, 
# then that link is false or the probability of a relationship between these entities is always zero. 
# We can immediately see problems with this assumption. 
# Once we assume this, we can’t predict any new links in the knowledge graph. 
# Collecting Real-world Data is a challenging task and lots of relationships are not captured in the 
# knowledge graph. This assumption turns all the missing data into false values.
# Local Closed World Assumption(LCWA) on the other hand, solves this problem by specifying a predicate 
# over areas that says whether the area of the knowledge graph is complete or not. 
# Stochastic Local Closed World Assumption(sLCWA) is a stochastic version of the LCWA.


from pykeen.training import SLCWATrainingLoop
training_loop = SLCWATrainingLoop(
    model=model,
    triples_factory=training_triples_factory,
    optimizer=optimizer,
)


# ## Experiment training with different epochs and batch sizes

# Train it now
_ = training_loop.train(
    triples_factory=training_triples_factory,
    num_epochs=5,
    batch_size=256,
)


# Pick an evaluator
# 'Nations' dataset also has a test set that can be used for evaluation  
from pykeen.evaluation import RankBasedEvaluator
evaluator = RankBasedEvaluator()

# Get triples to test
mapped_triples = dataset.testing.mapped_triples


## Evaluate the results obtained by printing and inspecting it


evaluation_results = evaluator.evaluate(model, mapped_triples, batch_size=256, additional_filter_triples=[dataset.training.mapped_triples])
#print(evaluation_results)


# In[59]:


## PyKeen pipeline provides a high-level entry point to access the models. It is an alternative to the above


result = pipeline(
   training= dataset.training,
   testing=  dataset.testing ,
   model = 'TransE',
   model_kwargs=dict(embedding_dim=2),
   random_seed=1,
   device='cpu',    
)


# ## Explore 'RotatE' instead of 'TransE' as a new model and note your observations


# First comes the 'TransE'
model= result.model

# Predict the tail
df = get_tail_prediction_df(result.model, 'brazil', 'accusation', triples_factory=result.training)
#print(df)


# train new 'RotatE' model
result = pipeline(
    dataset='Nations',
    model='RotatE', epochs= 5
)
model= result.model

# Then predict the tail
df = get_tail_prediction_df(result.model, 'brazil', 'accusation', triples_factory=result.training)
#print(df)


df = get_head_prediction_df(result.model, 'accusation', 'brazil', triples_factory=result.training)
#print(df)


df = get_relation_prediction_df(result.model, 'brazil', 'uk', triples_factory=result.training)
#print(df)


# Get scores for *all* triples
df = get_all_prediction_df(model, triples_factory=result.training)
#print(df)


# Get scores for top 15 triples
top_df = get_all_prediction_df(model, k=15, triples_factory=result.training)
#print(top_df)



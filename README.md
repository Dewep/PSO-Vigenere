# PSO-Vigenere

Applications of Particle Swarm Optimisation in Cryptanalysis - Vigenere cipher

## Usage

```bash
$> python app.py
Usage:  app.py -enc|-dec plain_file key
        app.py -pso cipher_file key_size nb_turn
```

## Example

```bash
$> python app.py -enc data/english.txt mypassword > data/english.enc

$> python app.py -pso data/english.enc 10 15
Turn=0          Key=sqvvbjspyg          Fitness=1479
Turn=1          Key=sqvvbjsoyg          Fitness=1805
Turn=2          Key=sqvsbjsoyg          Fitness=2119
Turn=3          Key=sqvsbjcoyg          Fitness=2383
Turn=4          Key=sqvsbjcorg          Fitness=2574
Turn=5          Key=sqvsbkcorg          Fitness=2750
Turn=6          Key=sqvsbkcord          Fitness=2927
Turn=7          Key=mqvsbkcord          Fitness=3360
Turn=8          Key=mqvswkcord          Fitness=3426
Turn=9          Key=myvswkcord          Fitness=3473
Turn=10         Key=mypswkcord          Fitness=3766
Turn=11         Key=mypawkcord          Fitness=4089
Turn=12         Key=mypaskcord          Fitness=4300
Turn=13         Key=mypasscord          Fitness=4703
Turn=14         Key=mypassword          Fitness=5221

Key=mypassword
your essay must include a brief definition of the type of problem being solved by the swarm intelligence algorithm as well as discussing how a candidate solution is represented by a particle in the case of pso or an ant in the case of aco and how the evaluation of a candidate solution is computed by a fitness quality function. in the case of aco using a local heuristic function, this should be discussed too. your essay must also discuss the strengths and weaknesses of the discussed types of swarm intelligence algorithms in the context of the application or type of problems addressed in your essay. note that there is no need to explain, in this short essay, concepts or applications that were already explained in the lectures.
```

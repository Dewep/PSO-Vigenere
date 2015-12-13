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

$> python app.py -pso data/english.enc 10
Key=ecjxksweis          Fitness=82
Key=ecjxkswois          Fitness=102
Key=ecjxsswois          Fitness=119
Key=ecjasswois          Fitness=146
Key=eyjasswois          Fitness=162
Key=eypasswois          Fitness=181
Key=mypasswois          Fitness=195
Key=mypasswoid          Fitness=209
Key=mypassword          Fitness=249

Key=mypassword
your essay must include a brief definition of the type of problem being solved by the swarm intelligence algorithm as well as discussing how a candidate solution is represented by a particle in the case of pso or an ant in the case of aco and how the evaluation of a candidate solution is computed by a fitness quality function. in the case of aco using a local heuristic function, this should be discussed too. your essay must also discuss the strengths and weaknesses of the discussed types of swarm intelligence algorithms in the context of the application or type of problems addressed in your essay. note that there is no need to explain, in this short essay, concepts or applications that were already explained in the lectures.
```

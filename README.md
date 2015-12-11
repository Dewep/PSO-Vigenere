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

$> python app.py -pso data/english.enc 10 25
Turn=0          Key=joatrfbeoy          Fitness=10004
Turn=1          Key=joatrfbeod          Fitness=9906
Turn=2          Key=joatrfbegd          Fitness=9851
Turn=3          Key=jqatrfbegd          Fitness=9685
Turn=4          Key=jqaerfbegd          Fitness=9638
Turn=5          Key=jqaerfkegd          Fitness=9515
Turn=6          Key=jqverfkegd          Fitness=9439
Turn=7          Key=gqverfkegd          Fitness=9178
Turn=8          Key=gqverfkhgd          Fitness=8859
Turn=9          Key=gqvbrfkhgd          Fitness=8704
Turn=10         Key=gqvbrfkhgd          Fitness=8704
Turn=11         Key=gqvbrfkhgd          Fitness=8704
Turn=12         Key=gqvbwfkhgd          Fitness=8552
Turn=13         Key=gqvbwfkhgd          Fitness=8552
Turn=14         Key=gyvbwfkhgd          Fitness=8477
Turn=15         Key=gyvbwfkhcd          Fitness=8299
Turn=16         Key=gypbwfkhcd          Fitness=8108
Turn=17         Key=mypbwfkhcd          Fitness=7687
Turn=18         Key=mypawfkhcd          Fitness=7287
Turn=19         Key=mypawskhcd          Fitness=7137
Turn=20         Key=mypasskhcd          Fitness=6589
Turn=21         Key=mypasswhcd          Fitness=6347
Turn=22         Key=mypasswocd          Fitness=5858
Turn=23         Key=mypassword          Fitness=5261
Turn=24         Key=mypassword          Fitness=5261

Key=mypassword
your essay must include a brief definition of the type of problem being solved by the swarm intelligence algorithm as well as discussing how a candidate solution is represented by a particle in the case of pso or an ant in the case of aco and how the evaluation of a candidate solution is computed by a fitness quality function. in the case of aco using a local heuristic function, this should be discussed too. your essay must also discuss the strengths and weaknesses of the discussed types of swarm intelligence algorithms in the context of the application or type of problems addressed in your essay. note that there is no need to explain, in this short essay, concepts or applications that were already explained in the lectures.
```

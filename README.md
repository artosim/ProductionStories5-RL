# Training 

- ppo_example.py - код тренировки
- ./tmp/ppo/dungeon - checkpoints
- ./save/train/ray_results - ray logging
- ./save/train/gifs - gif-результаты
- ./tf_training - tensorflow: логгирование тренировки
- ./tf_trajectory - tensorflow: логгирование траектории


## Example:


python ppo_example.py \
--seed 666 \
--n_iter 500 \
--env Dungeon \
--agent_ckpt_dir ./tmp/ppo/dungeon \
--train_gif_dir ./save/train/gifs \
--ray_result_dir ./save/train/ray_results



#### Files

- ./mapgen/mapgen/agent.py - агент
- ./mapgen/mapgen/env.py - стандартное окружение
- ./mapgen/mapgen/dungeon.py - генератор среды
- ./mapgen/mapgen/map.py - карта

# Results

Для экспериментов был применен алгоритм PPO, который был рассказан на лекции.
Эксперименты проводились со следующими наградами: стандартная + штраф за время, награда со слайда 21 лекции.

Результаты представлены на графиках в ноутбуке [/Results.ipynb](./Results.ipynb)

Из них мы можем видеть, что средняя длина эпизода для второй награды меньше первой. Показалось, что изменение награды улучшило работу алгоритма, но если посмотреть на траектории движения:
Итерация 5
 ![Iteration 5](./save/train/gifs/005.gif)
 Итерация 100
 ![Iteration 100](./save/train/gifs/100.gif)
 
 То мы можем видеть, что агент просто останавливается.
 
 Может быть для лучших результатов надо дольше обучать агента на тех же наградах.

import numpy as np
import random
import torch
    

def update_writer_training(writer, result, n):
    n +=1        
         
    lst = ["episode_reward_min",
           "episode_reward_mean",
           "episode_reward_max",
           "episode_len_mean",
           "episodes_this_iter",
           "episodes_total",
           "training_iteration"]    
    
    for key in lst:
        writer.add_scalar(key, result[key], n)

    dct = result['info']['learner']['default_policy']['learner_stats']
    for key, value in dct.items():
        writer.add_scalar(key, value, n)

    return writer



def update_writer_trajectory(writer_trajectory, info, reward, _):

    info["total_unexplored"] = info["total_cells"] - info["total_explored"]
    info["total_explored_%"] = info["total_explored"] / info["total_cells"] 
    info["new_explored_abs_%"] = info["new_explored"] / info["total_cells"]
    info["new_explored_relative_%"] = info["new_explored"] / (info["total_unexplored"] + info["new_explored"])
    
    writer_trajectory.add_scalar("reward", reward, _)
    
    for key, value in info.items():
        if type(value) == bool:
            value = int(value)
        writer_trajectory.add_scalar(key, value, _)
    
    return writer_trajectory
   
    
    
def seed_everything(seed, env=None):
    if env is not None:
        env.seed(seed)
        env.action_space.seed(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    
    

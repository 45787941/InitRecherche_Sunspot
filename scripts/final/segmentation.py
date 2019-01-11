import watershed
import level_sets
import expected_data

labels = ['expected_data', 'watershed', 'level_sets']

def all(path = ''):
    return [expected_data.compute(path), watershed.compute(path), level_sets.compute(path)]

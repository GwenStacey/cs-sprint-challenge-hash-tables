def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weights_indices = {}
    for i in range(length):
        if weights[i] not in weights_indices.keys():
            weights_indices[weights[i]] = [i]
        else:
            weights_indices[weights[i]].append(i)
    for i in weights_indices.keys():
        if limit-i in weights_indices.keys():
            if len(weights_indices[i]) > 1:
                if weights_indices[i][0]>weights_indices[i][1]:
                    return (weights_indices[i][0], weights_indices[i][1])
                else:
                    return (weights_indices[i][1], weights_indices[i][0])
            if weights_indices[i] > weights_indices[limit-i]:
                return (weights_indices[i][0], weights_indices[limit-i][0])
            else:
                return (weights_indices[limit-i][0], weights_indices[i][0])

    

    return None

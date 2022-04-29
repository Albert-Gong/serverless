/**
 * Created on 2022/4/22.
 * @author Zhihao Gong
 * @changeLogs
 */

import center_lake from "@/assets/images/center_lake.png"
import museum from "@/assets/images/museum.png"
import colosseum from "@/assets/images/colosseum.jpg"
import library from "@/assets/images/library.jpg"
import overlook from "@/assets/images/overlook.jpg"

let random_list = [
    center_lake, museum, colosseum, library, overlook
]

let random_choice = ()=>{
    if ( Math.random() < 0.2) return random_list[0]
    if ( Math.random() < 0.4) return random_list[1]
    if ( Math.random() < 0.6) return random_list[2]
    if ( Math.random() < 0.8) return random_list[3]
    return random_list[4]

}

const preprocess_apis = [
    {
        api_id: 0,
        api_name: "normalize",
        api_des: "This api is used to normalize data",
        image: random_choice()
    },
    {
        api_id: 1,
        api_name: "standardizing",
        api_des: "This api is used to find outliers",
        image: random_choice()
    },
    {
        api_id: 2,
        api_name: "rescale",
        api_des: "rescale",
        image: random_choice()
    },
    {
        api_id: 3,
        api_name: "discrete",
        api_des: "discretize data",
        image: random_choice()
    },
    {
        api_id: 4,
        api_name: "groupby",
        api_des: "abc",
        image: random_choice()
    },
    {
        api_id: 5,
        api_name: "groupCount",
        api_des: "abc",
        image: random_choice()
    },
    {
        api_id: 6,
        api_name: "smooth",
        api_des: "smooth data",
        image: random_choice()
    },
    {
        api_id: 7,
        api_name: "removeRedundance",
        api_des: "remove redundant data ",
        image: random_choice()
    },
    {
        api_id: 8,
        api_name: "correlation",
        api_des: "explore correlation",
        image: random_choice()
    },
    {
        api_id: 9,
        api_name: "ismissing",
        api_des: "abc",
        image: random_choice()
    },
    {
        api_id: 10,
        api_name: "rmmissing",
        api_des: "remove missing items",
        image: random_choice()
    },
    {
        api_id: 11,
        api_name: "fillmissing",
        api_des: "fill missing items",
        image: random_choice()
    },
    {
        api_id: 12,
        api_name: "isoutliers",
        api_des: "abc",
        image: random_choice()
    },
    {
        api_id: 13,
        api_name: "rmoutliers",
        api_des: "remove outliers",
        image: random_choice()
    },
    {
        api_id: 14,
        api_name: "filloutliers",
        api_des: "fill outliers",
        image: random_choice()
    },
    {
        api_id: 15,
        api_name: "movmad",
        api_des: "move mean with deviation",
        image: random_choice()
    },
    {
        api_id: 16,
        api_name: "movmean",
        api_des: "move mean",
        image: random_choice()
    },
    {
        api_id: 17,
        api_name: "movmedian",
        api_des: "move median",
        image: random_choice()
    },
    {
        api_id: 18,
        api_name: "pca",
        api_des: "reduce dimension",
        image: random_choice()
    },
    {
        api_id: 19,
        api_name: "basic",
        api_des: "return max, min, mean and std",
        image: random_choice()
    }
]


export {
    preprocess_apis,
}

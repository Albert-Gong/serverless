/**
 * Created on 2022/4/21.
 * @author Zhihao Gong
 * @changeLogs
 */

import museum from "@/assets/images/museum.png"
import ai from "@/assets/images/ai.jpeg"

const services = [
    {
        name: "Preprocess",
        description: `The Preprocess section is to preprocess data for data analysis. Here we provide 20 apis for 
                      you to use. It is convenient as you only need to upload a txt or csv file containing the data
                      you want to process. With the help the Huawei function graphs, you can get your answer in no time`,
        image: ai,
    },
    {
        name: "AI reference",
        description: "You can use ai models to do refence tasms such sentiment analysis",
        image: ai,
    },
    {
        name: "Pipeline",
        description: "Here we use function graphs to construct cascading function calls",
        image: ai,
    }
]


let  token_data =
    {
        "auth":
            {
                "identity":
                    {
                        "password":
                            {
                                "user":
                                    {
                                        "domain":
                                            {
                                                "name": "1"

                                            },
                                        "name": "2",
                                        "password": "3"
                                    }
                            },
                        "methods": ["password"]
                    },
                "scope":
                    {
                        "project":
                            {
                                "name": "cn-north-4"
                            }
                    }
            }
    }


export
{
    services,
    token_data
}



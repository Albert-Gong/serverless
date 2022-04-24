/**
 * Created on 2022/4/21.
 * @author Zhihao Gong
 * @changeLogs
 */

import museum from "@/assets/images/museum.png"

const services = [
    {
        name: "Preprocess",
        description: `Preprocess part is to preprocess data for data analysis. Here we provide over 20 apis for 
                      you to call. It is convenient as you only need to upload a txt or csv file containing the data
                      you want to process. With the help the Huawei serverless apis, you can get your answer in no time`,
        image: museum,
    },
    {
        name: "AI reference",
        description: "You can use ai models to do some basic tasks such sentiment analysis",
        image: museum,
    },
    {
        name: "Pipeline",
        description: "To do",
        image: museum,
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



import base_url from "./api/base_url";

export const analyzeProject = async (data)=>{
    console.log("analyze project")
    const res = await fetch(`${base_url}/analyze`, {
        method:"POST",
        headers : {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    })

    if(!res.ok){
        throw new Error("Server error");
    }

    console.log("api analyze project")

    return res.json()
}
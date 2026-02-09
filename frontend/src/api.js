import base_url from "./api/base_url";

export const analyzeProject = async (data)=>{
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

    return res.json()
}
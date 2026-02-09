export default api = 'http://127.0.0.1:8000/analyze'

export const analyzeProject = async (data)=>{
    const res = await fetch(`${api}`, {
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


async function getCupcakes(){
     cupcake_list = await axios.get("/api/cupcakes")
     for(x=0; x < cupcake_list.data.cupcake.length; x++){
          c = cupcake_list.data.cupcake[x].flavor
          $("#cupcakes-list").append(`<li>
          <p>${c}</p>
          <img src="${cupcake_list.data.cupcake[x].image}">
          </li>`)
     }
    return $("cupcakes-list").append(`<li>{cupcake.data[0].flavor}</li>`)
}

$("#cupcake-list-btn").on("click",getCupcakes)

async function createCupcake(event){
     event.preventDefault()
     let flavor = $('#flavor').val()
     let size = $('#size').val()
     let rating = $('#rating').val()
     let image = $('#image').val()
     let cupcakeList = {cupcake:[{flavor, size, rating, image}]}
     
     console.log(cupcakeList)
     
     await axios.post("/api/cupcakes",
          cupcakeList
     )
     
     await getCupcakes()

}


$('#new-cupcake').on('submit', createCupcake, event)

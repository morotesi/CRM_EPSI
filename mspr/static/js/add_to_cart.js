const checkIfLocalstorage  = () => localStorage.length > 0 ? true : false;

const getItemsInLocalStorage = () =>{
   const voitures =localStorage.getItem('voitureInCart');
   return voitures;
}

const getNbrItemsInLocalStorage =() =>{
    const nbrItems =localStorage.getItem('nbrVoitureInCart');
    return nbrItems;
}

const getVoituresInCard =()=>{
    const voituresJson = localStorage.getItem('voitureInCart');
    return voituresJson;
}

const parseAndFormatProductsInCard =()=>{
    const voituresJson = getVoituresInCard();
    const items =Object.values(JSON.parse(getVoituresInCard));
    return items;
}

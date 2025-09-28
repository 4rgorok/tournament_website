import React, { useState, useEffect } from 'react';
import { BASE_URL } from "../../utils";
import axios from 'axios';

import './TatamiCategory.css';

const TatamiCategory = ({ id, type }) => {
    const [category, setItems] = useState([]);

    useEffect(() => {
        if(type == 'kata'){
            axios.get(BASE_URL+'/api/kata')
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
        
        }
        else if(type == 'kumite'){
            axios.get(BASE_URL+'/api/kumite/fight/'+id)
            .then(response => setItems(response.data))
            .catch(error => console.error('Error fetching data:', error));
        }
    }, []);
    if(category != undefined)
    {
        return (
            <h2 className='category' key={category.id}>{category.groupname}</h2>
        );
    }
};

export default TatamiCategory;
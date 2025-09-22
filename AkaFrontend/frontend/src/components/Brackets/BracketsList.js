import React, { useState, useEffect } from 'react';
import { BASE_URL } from "../../utils";
import './BracketsList.css';
import axios from 'axios';

import {Link} from "react-router-dom";



const BracketsList = ({ id }) => {
  const [brackets, setItems] = useState([]);
    useEffect(() => {
        axios.get(BASE_URL+'/api/kumite', {
      }
      )
      .then(response => setItems(response.data))
      .catch(error => console.error('Error fetching data:', error));
 
    }, []);
  console.log(brackets)
  if(brackets[0] != undefined){
    
    return (
        <div className='bracketsWrapper'>
        
        {brackets.map(bracket => (
            <div className='qwe'>
                <Link className={"brackets"} to={"/brackets/" + bracket.id} > {bracket.groupname} </Link><br /><br />
            </div>
        ))}
                    
        </div>
    );
  } 
};

export default BracketsList;

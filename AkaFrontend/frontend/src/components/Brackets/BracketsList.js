import React, { useState, useEffect } from 'react';
import { BASE_URL } from "../../utils";
import './BracketsList.css';
import Brackets from './BracketsHome';
import axios from 'axios';

import {Link} from "react-router-dom";



const BracketsList = ({ id }) => {
  const [brackets, setItems] = useState([]);
  const [selectedBracketId, setSelectedBracketId] = useState(null);
    useEffect(() => {
      axios.get(BASE_URL+'/api/kumite')
      .then(response => {
        setItems(response.data)
        if (response.data.length > 0) {
          setSelectedBracketId(response.data[0].id);
        }
      })
      .catch(error => console.error('Error fetching data:', error));
 
    }, []);

  const handleSelectChange = (event) => {
    setSelectedBracketId(parseInt(event.target.value));
  };

  if (brackets.length === 0) {
    return null; // or a loading indicator
  }
    
  return (
    <>
      <div className='bracketsWrapper'>
        <select 
          value={selectedBracketId || ''} 
          onChange={handleSelectChange}
          className="bracket-select"
        >
          {brackets.map(bracket => (
            <option key={bracket.id} value={bracket.id}>
              {bracket.groupname}
            </option>
          ))}
        </select>
      </div>
      {selectedBracketId && <Brackets key={selectedBracketId} id={selectedBracketId} />}
    </>
  );
   
};
/*
<div className='qwe'>
<Link className={"brackets"} to={"/brackets/" + bracket.id} > {bracket.groupname} </Link><br /><br />
</div>
*/
export default BracketsList;

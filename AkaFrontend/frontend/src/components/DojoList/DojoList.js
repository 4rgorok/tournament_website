import React, { useState, useMemo, useCallback } from 'react';
import axios from 'axios';
import { BASE_URL } from "../../utils";

import './DojoList.css';

const DojoList = ({ onClubSelect }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [clubs, setClubs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  // Fetch all clubs on component mount
  React.useEffect(() => {
    const fetchClubs = async () => {
      setIsLoading(true);
      try {
        const response = await axios.get(BASE_URL + '/api/dojo');
        setClubs(response.data);
      } catch (error) {
        console.error('Error fetching clubs:', error);
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchClubs();
  }, []);

  // Filter clubs based on search term
  const filteredClubs = useMemo(() => {
    if (!searchTerm.trim()) return [];
    
    const term = searchTerm.toLowerCase();
    return clubs.filter(club => 
      club.dojoname.toLowerCase().includes(term)
    ).slice(0, 10); // Limit results to 10
  }, [clubs, searchTerm]);

  const handleInputChange = useCallback((e) => {
    setSearchTerm(e.target.value);
  }, []);

  const handleClubSelect = useCallback((club) => {
    onClubSelect(club);
    setSearchTerm('');
  }, [onClubSelect]);

  return (
    <div className="club-selector">
      <input
        type="text"
        placeholder="Wyszukaj swój klub po nazwie..."
        value={searchTerm}
        onChange={handleInputChange}
        className="club-search-input"
      />
      
      {isLoading && <div>Loading clubs...</div>}
      
      {searchTerm && filteredClubs.length > 0 && (
        <div className="club-results">
          {filteredClubs.map(club => (
            <div 
              key={club.id} 
              className="club-result-item"
              onClick={() => handleClubSelect(club.id)}
            >
              {club.dojoname}
            </div>
          ))}
        </div>
      )}
      
      {searchTerm && filteredClubs.length === 0 && !isLoading && (
        <div className="no-results">No clubs found matching "{searchTerm}"</div>
      )}
    </div>
  );
};

export default DojoList;
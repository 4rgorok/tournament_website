import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useParams } from 'react-router-dom';

import TatamiList from './components/Tatami/TatamiList';
import Brackets from './components/Brackets/BracketsHome';
import BracketsList from './components/Brackets/BracketsList';
import Layout from './components/Layout/Layout';
import HamburgerMenu from './components/Menu/Menu';
import DojoList from './components/DojoList/DojoList';
import Contestants from './components/Contestants/Contestants';


const BracketsWrapper = () => {
  const { id } = useParams();
  return <Brackets id={id} />;
};

const TatamiListPage = () => (
  <>
  <HamburgerMenu/>
  <TatamiList />
  </>
  
);

const BracketsListPage = () => (
 <>
  <HamburgerMenu/>
  <BracketsList />
  </>
);

const DojoPage = ({routeChange}) => (
  <>
  <HamburgerMenu/>
  <DojoList onClubSelect={routeChange}/>
  </>
);

const ContestantWrapper = () => {
  const { id } = useParams();
  return (<>
  <HamburgerMenu/>
  <Contestants dojo_id={id} />
  </>);
};


const App = () => {
  let navigate = useNavigate(); 
  const routeChange = (id) =>{ 
    let path = `/dojo/`+id; 
    navigate(path);
  }
  return (
      <Routes>
        <Route path="/" element={<TatamiListPage />} />
        <Route path="/brackets" element={<BracketsListPage />} />
        <Route path="/dojolist" element={<DojoPage routeChange = {routeChange}/>} />
        <Route path="/dojo/:id" element={<ContestantWrapper />} />
      </Routes>
  );
};

export default App;

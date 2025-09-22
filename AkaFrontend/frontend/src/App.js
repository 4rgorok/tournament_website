import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useParams } from 'react-router-dom';

import TatamiList from './components/Tatami/TatamiList';
import Brackets from './components/Brackets/BracketsHome';
import BracketsList from './components/Brackets/BracketsList';
import { Bracket } from 'react-brackets';

const BracketsWrapper = () => {
  const { id } = useParams();
  return <Brackets id={id} />;
};

const App = () => {
  return (
    <BrowserRouter>
          <Routes>
              <Route path="/" exact element={<TatamiList />} />
              <Route path="/brackets" exact element={<BracketsList />} />
              <Route path="/brackets/:id" element={<BracketsWrapper/>} />
          </Routes>
    </BrowserRouter>
  );
};

export default App;

import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import TatamiList from './components/Tatami/TatamiList';
import Brackets from './components/Brackets/BracketsHome';

const App = () => {
  return (
    <BrowserRouter>
          <Routes>
              <Route path="/" exact element={<TatamiList />} />
              <Route path="/brackets" exact element={<Brackets />} />
          </Routes>
    </BrowserRouter>
  );
};

export default App;

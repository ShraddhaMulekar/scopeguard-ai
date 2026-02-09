import { BrowserRouter, Route, Routes } from "react-router-dom";
import DebugLocation from "./pages/DebugLocation";
import ResultPage from "./pages/ResultPage";
import AnalyzePage from "./pages/AnalyzePage";


function App() {

  return (
    <BrowserRouter>
      <DebugLocation />
      <Routes>
        <Route index element={<AnalyzePage />} />
        <Route path="/result" element={<ResultPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

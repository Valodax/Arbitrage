import { DAppProvider, Config, Kovan } from "@usedapp/core"
import { Header } from "./components/Header";
import { Container } from "@material-ui/core";
import { Main } from "./components/Main";
import { getDefaultProvider } from 'ethers'


const config: Config = {
  readOnlyChainId: Kovan.chainId,
  readOnlyUrls: {
    [Kovan.chainId]: getDefaultProvider('kovan'),
  },
}

function App() {
  return (
    <DAppProvider config={config} >
      <Header></Header>
      <Container maxWidth="md">
        <div className="App">
          <Main />
        </div>
      </Container>
    </DAppProvider>
  );
}

export default App;

import React from "react";

const Example = (props: {title : string}) => {
    return <div>{props.title}</div>
}

const App = () => {
  return <Example title="Needz api"/>
};

export default App;

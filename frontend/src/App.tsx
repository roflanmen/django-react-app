import React from "react";

const Example = (props: {title : string, number: number}) => {
    return <div>{props.title} {props.number}</div>
}

const App = () => {
    const [data, setData] = React.useState("");
    React.useEffect(() => {
        fetch("/api/test")
            .then((res) => res.text())
            .then((data) => setData(data));
    }, []);
    return <div>{data}</div>;
};
// const App = () => {
//   return <Example title="Hello World" number={23}/>
// };

export default App;

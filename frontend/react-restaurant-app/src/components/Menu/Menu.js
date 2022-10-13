import { useState } from "react";
import MenuSelect from "./MenuSelect";
import MenuItem from "./MenuItem";

function Menu({ menuItems, ...props }) {
    const [select, setSelect] = useState(null);

    const updateSelect = (value) => {
      setSelect(value);
    };

    const menuList = menuItems
    .filter((item) => select ? item.type === select : item)
    .map((item) => <MenuItem key={item.id} item={item} updateOrder={props.updateOrder} />);

  return (
    <div>
      <section className="main-menu">
          <MenuSelect updateSelect={updateSelect}/>
          <ul className="menu-list">{menuList}</ul>
      </section>
    </div>
  );
}

export default Menu;
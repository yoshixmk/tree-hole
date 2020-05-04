import * as React from 'react';
import ListItem from './ListItem';
import { User } from '../interfaces';

type Props = {
  items: Array<User>;
};

const List: React.FunctionComponent<Props> = ({ items }: Props) =>
  <ul>
    {items.map((item: User) =>
      <li key={item.id}>
        <ListItem data={item} />
      </li>
    )}
  </ul>;


export default List;

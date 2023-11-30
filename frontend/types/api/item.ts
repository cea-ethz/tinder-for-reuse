/////////////////////////////////////////////////////////////////////////////
// Do not modify this file directly. It is created from the API definition //
/////////////////////////////////////////////////////////////////////////////

import { AccountRead } from "./account";
import { TypeRead } from "./type";

/////////////////////////////////////////////////////////////////////////////
// See: ./shared/schemas/item_schema.ts                                    //
/////////////////////////////////////////////////////////////////////////////

type ItemImageBase = {
  url: string;
};

type ItemImageCreate = ItemImageBase;

type ItemBase = {
  title: string;
  description?: string;
};

export type ItemCreate = ItemBase & {
  category_type_id: number;
  images?: ItemImageCreate[];
};

/////////////////////////////////////////////////////////////////////////////
// See: ./backend/app/schemas/item_schema.py                               //
/////////////////////////////////////////////////////////////////////////////

export type ItemImageRead = ItemImageBase & {
  is_best: boolean;
};

export type ItemRead = ItemBase & {
  id: number;
  category_type: TypeRead;
  account?: AccountRead;
  images?: ItemImageRead[];
};
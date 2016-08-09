class CreateHtmlPages < ActiveRecord::Migration[5.0]
  def change
    create_table :html_pages do |t|
      t.references :session, foreign_key: true
      t.text :dom

      t.timestamps
    end
  end
end

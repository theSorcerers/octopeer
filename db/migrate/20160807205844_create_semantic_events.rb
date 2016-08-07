class CreateSemanticEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :semantic_events do |t|
      t.references :session, foreign_key: true
      t.references :event_type, foreign_key: true
      t.references :element_type, foreign_key: true

      t.timestamps
    end
  end
end

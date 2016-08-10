class Api::SemanticEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def semantic_event_params
    params.require(:semantic_event).permit(:session_id, :event_type_id, :element_type_id, :created_at)
  end
end

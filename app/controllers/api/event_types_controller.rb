class Api::EventTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def event_type_params
    params.require(:event_type).permit(:id, :name)
  end
end

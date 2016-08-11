class Api::ElementTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:element_type).permit(:name)
  end
end
